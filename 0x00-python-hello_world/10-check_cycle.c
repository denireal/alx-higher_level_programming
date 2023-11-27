#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		/* Move slow by one step and fast by two steps */
		slow = slow->next;
		fast = fast->next->next;

		/* If there is a cycle, find the starting node of the cycle */
		if (slow == fast)
		{
			slow = list;
			while (slow != fast)
			{
				slow = slow->next;
				fast = fast->next;
			}
			return (1); /* Cycle detected */
		}
	}

	return (0); /* No cycle found */
}

