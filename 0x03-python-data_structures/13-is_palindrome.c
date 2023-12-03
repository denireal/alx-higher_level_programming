#include "lists.h"

/**
* reverse_listint - Reverses a linked list in place.
* @head: Pointer to the head of the linked list.
*/
void reverse_listint(listint_t **head)
{
listint_t *previous = NULL;
listint_t *current = *head;
listint_t *next = NULL;

for (; current; next = current->next, current->next = previous,
previous = current, current = next)
{

}

*head = previous;
}

/**
* is_palindrome - Checks if a linked list is a palindrome.
* @head: Pointer to the head of the linked list.
* Return: 1 if palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{
listint_t *slow_ptr = *head, *fast_ptr = *head;
listint_t *current_ptr = *head, *second_half = NULL;

if (*head == NULL || (*head)->next == NULL)
return (1);

/* Find the middle of the linked list */
for (;;)
{
fast_ptr = fast_ptr->next->next;
if (!fast_ptr)
{
second_half = slow_ptr->next;
break;
}
if (!fast_ptr->next)
{
second_half = slow_ptr->next->next;
break;
}
slow_ptr = slow_ptr->next;
}

/* Reverse the second half of the linked list */
reverse_listint(&second_half);

/* Compare the reversed second half with the first half */
for (; second_half && current_ptr; second_half = second_half->next,
current_ptr = current_ptr->next)
{
if (current_ptr->n != second_half->n)
return (0);
}

/* Check if the linked list is a palindrome */
return (!second_half);
}
